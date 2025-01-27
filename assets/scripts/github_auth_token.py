"""
Get a OAuth token from github using device flow
"""
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

from __future__ import annotations
import sys
import time
from dataclasses import dataclass
from typing import NoReturn
import logging
import requests

logger = logging.getLogger(__name__)

def handel_oauth_device_flow_error(
        resp_code: int, resp: dict, poll_interval: int) -> int | NoReturn:
    """
    Return the poll interval if should retry, otherwise exit the program
    """
    if resp_code != 400:
        logger.error("Failed in device flow, response code: %d", resp_code)
        logger.error("Response: %s", resp)
        sys.exit(-1)

    if resp["error"] == "authorization_pending":
        logger.info("Authorization pending, please authorize in the browser")
        return poll_interval
    if resp["error"] == "slow_down":
        logger.info(
            "Authorization pending, please wait for %d seconds", resp["interval"])
        return poll_interval + 5
    if resp["error"] == "expired_token":
        logger.error("Device code expired, please try again")
        sys.exit(-1)
    if resp["error"] == "unsupported_grant_type":
        logger.error("Something went wrong, contact the developer")
        logger.error("Provide the following information: %s", resp)
        sys.exit(-1)
    if resp["error"] == "incorrect_client_credentials":
        logger.error(
            "Incorrect client credentials, please check the client id")
        sys.exit(-1)
    if resp["error"] == "incorrect_device_code":
        logger.error("Incorrect device code, please check the device code")
        sys.exit(-1)
    if resp["error"] == "device_flow_disabled":
        logger.error("Device flow is disabled, please contact the admin")
        sys.exit(-1)
    logger.error("Unknown error, please contact the developer")
    logger.error("Provide the following information: %s", resp)
    sys.exit(-1)


@dataclass
class OAuthAPPBasic:
    client_id: str
    scope: str

    def __post_init__(self):
        if self.client_id is None:
            logger.error("client_id is required")
            raise ValueError("client_id is required")
        if self.scope is None:
            self.scope = ""

    __REQ_URL = "https://github.com/login/device/code"

    def post_request(self) -> OAuthDeviceFlowRequest | NoReturn:

        req = requests.post(self.__REQ_URL, data={
            "client_id": self.client_id,
            "scope": self.scope,
        },
            headers={
            "Accept": "application/json"
        }, timeout=10)

        if req.status_code != 200:
            handel_oauth_device_flow_error(req.status_code, req.json(), 0)
            sys.exit(-1)

        res = req.json()
        return OAuthDeviceFlowRequest(
            app=self,
            device_code=res["device_code"],
            user_code=res["user_code"],
            verification_uri=res["verification_uri"],
            expires_in=res["expires_in"],
            interval=res["interval"]
        )


@dataclass
class OAuthDeviceFlowRequest():
    app: OAuthAPPBasic
    device_code: str
    user_code: str
    verification_uri: str
    expires_in: int
    interval: int

    __POLL_URL = "https://github.com/login/oauth/access_token"

    def poll_once(self) -> None | OAuthDeviceFlowResponse:

        req = requests.post(self.__POLL_URL, data={
            "client_id": self.app.client_id,
            "device_code": self.device_code,
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code"
        },
            headers={
            "Accept": "application/json"
        }, timeout=10)

        if req.status_code != 200:
            new_interval = handel_oauth_device_flow_error(
                req.status_code, req.json(), self.interval)
            self.interval = new_interval
            return None

        res = req.json()
        return OAuthDeviceFlowResponse(
            app=self.app,
            access_token=res["access_token"],
            token_type=res["token_type"],
            scope=res["scope"]
        )

    def poll_until(self) -> OAuthDeviceFlowResponse | NoReturn:
        begin_time = time.time()
        while True:
            if time.time() - begin_time > self.expires_in:
                logger.error("Device code expired, please try again")
                sys.exit(-1)
            res = self.poll_once()
            if res is not None:
                return res
            time.sleep(self.interval)


@dataclass
class OAuthDeviceFlowResponse():
    app: OAuthAPPBasic
    access_token: str
    token_type: str
    scope: str


SCOPE = "repo,workflow"


def req_token():
    client_id = input("Enter your client_id: ")
    app = OAuthAPPBasic(client_id, SCOPE)
    req = app.post_request()
    logger.warning("Please authorize in the browser, visit the following url:")
    logger.warning(req.verification_uri)
    logger.warning("Enter the user code: %s", req.user_code)
    _ = input("Press enter to continue")
    res = req.poll_until()
    logger.warning("Access token: %s", res.access_token)
    logger.warning("Token type: %s", res.token_type)
    logger.warning("Scope: %s", res.scope)


if __name__ == "__main__":
    req_token()
