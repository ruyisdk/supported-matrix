## Ruyi Index Updater

This tool automatically updates the index file for mirrors in the ruyi tool, synchronizing the support matrix with the ruyi index.

### How to Use

You need to set the environment variable `GITHUB_TOKEN`, and this token must have read, write, and PR permissions for the relevant repository. Alternatively, you can enable permissions to allow the tool to fork the repository automatically.

**Note!** Tokens get directly from Github settings are personal tokens, which will be rejected when making PRs to organization repositories. You need to use an OAuth app token. The easiest way to distinguish them is by format: personal tokens start with `ghp`, while OAuth app tokens start with `gho`. 

If want to test only, you can use the `gh` command-line tool to get one. **Be careful not to leak the token, it has all permission of your account if you get it from `gh` tool.**; Create an OAuth app and use it as described below.

By default, the tool operates in a temporary directory, which might involve downloading many mirror files each time. You can set the environment variable `CACHE_DIR` to specify a cache directory, and the tool will store everything there.

The `renew_ruyi_index.py` script encapsulates all operations, and you can run this script directly. The parameters are as follows:
- `-c` or `--config`: Path to the configuration file, which can be shared with nvchecker. The primary focus is on the `[vendor-system-variance]` field.
- `-p` or `--path`: Path to the support matrix.
- `-i` or `--index`: Path to the new ruyi index to be uploaded (excluding the `ruyi-index` part). If not specified, a new one will be cloned in the temporary folder.
- `--pr`: Whether to directly submit a PR. If not specified, the PR content will be displayed in the console. **Since the PR includes an identifier to prevent duplicate PRs, please make sure to include this identifier!**

### Plugin Development Guide

Due to the complexity of mirror mapping (a single report might correspond to multiple files or indices) and version numbers that need manual handling, creating plugins for each mirror is currently necessary. In the future, generic plugin development may be considered.

To add a new plugin, simply create a new file in the `ruyi_index_updater/upload_plugin` directory. You can directly import the `prelude` from the current folder for some typing helpers.

A `register` function is mandatory in the file. If it returns `Null`, it indicates that the plugin should not be loaded (you can add logic checks if needed). Otherwise, it should return an instance of `UploadPluginBase`.

In the `UploadPluginBase` class, you need to implement the following methods:
- `get_name`: A static method that returns the name of the plugin.
- `can_handle`: Determines if the current mirror can be handled (stored as a vendor-system-variance triplet, including the original report in `raw_data`).
- `is_mapped_ruyi_index`: Checks if a mirror in the current ruyi index can be generated from the report.
- `handle_version`: Maps the mirror version to the semantic version used by ruyi. For more definitions, refer to ruyi documentation.
- `handle_report`: Uses the current report to generate a new image index for the ruyi index.

You can review the provided helper functions as needed. An example plugin is provided for the LPI4A system in ruyi, which includes RevyOS and two U-Boot mirrors. The RevyOS mirror contains multiple files, making it a good representation of all scenarios.

## How to Use an OAuth APP

The following explains how to use an OAuth APP and obtain a token.

### Confirm the Type of Account You Want to Use

Due to Github's permission limitation, all permissions are **bound to users** (including organizations). This means you cannot have a token for an organization but only for your user account. Therefore, for the Github account you authorize, make sure it is a user account, not an organization account.

If you do not want to use your main account, feel free to create a new account. Github provides a special exception for bot accounts, which does not violate the one account per person policy:
> User accounts are intended for humans, but you can create accounts to automate activity on GitHub. This type of account is called a machine user. For example, you can create a machine user account to automate continuous integration (CI) workflows.

### Create an OAuth APP

Open your account settings and find Developer settings:
![1](img/1.png)

Enter and select OAuth Apps:
![2](img/2.png)

Click New OAuth App:
![3](img/3.png)

Fill in the information as needed. The Authorization callback URL can be anything, such as `http://127.0.0.1:12345`. **Be sure to check Enable Device Flow**:
![4](img/4.png)

Register the APP, get the Client ID:
![5](img/5.png)

### Use the OAuth APP

In `src/ruyi_index_updater/github_auth.py` is a separate script that is used to obtain a token. Simply run it and follow the prompts to input the required information.
```python
python assets/src/ruyi_index_updater/github_auth.py
```
