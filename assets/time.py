"""
main
"""

import argparse
import os
from urllib.parse import urljoin
from src.svg_gen import SvgConf, SvgNode, SvgXml, gen_html, putconf, SvgRectContainer
from src.svg_gen import SvgText, SvgTextCenter, SvgMoveTo, SvgCR, SvgLF, SvgGroup
from src.svg_gen import SvgAdvancer, SvgSvg, SvgLine, SvgLink
from src.matrix_parser import Systems, status_map
from datetime import datetime, timedelta

def gen_color(_, col, content):
    """
    gen svg color
    """
    white = 'rgb(255, 255, 255)'
    gray = 'rgb(220, 220, 220)'
    green = 'rgb(0, 255, 0)'
    red = 'rgb(255, 0, 0)'
    if col < 3:
        return white
    if content=='N/A':
        return gray
    index=content.find(':')
    if index != -1:
        content=content[index+2:]
    now = datetime.now()
    dt_obj = datetime.strptime(content, '%Y-%m-%d')
    life=(now-dt_obj).days
    if life==0:
        return green
    if life<=90:
        return 'rgb('+str(255*life/90)+', '+str(255)+', '+str(0)+')'
    if life<=180:
        return 'rgb('+str(255)+', '+str(255-255*life/90)+', '+str(0)+')'
    if life>180:
        return red
    return gray


def gen_link(_, __, content):
    """
    gen link
    """
    if hasattr(content, 'link') and content.link is not None:
        url = "https://github.com/ruyisdk/support-matrix/tree/main/"
        for i in content.link:
            url = urljoin(url + '/', i)
        return url
    return None


def gen_svg_table(conf: SvgConf, systems: Systems, need_systems: dict[str]) -> SvgNode:
    """
    Generate a svg table with the given systems
    """
    putconf(conf)

    table = []

    head_row = [
        "CPU",
        "IP Core",
        "Product/Model",
    ]
    for i in need_systems.values():
        head_row.append(i)
    head_group = []
    for idx, i in enumerate(head_row):
        t = SvgText(i, True)
        head_group.append(t)
    table.append(head_group)

    for board in systems.boards:
        syscnt = 0
        for system in board.systems:
            if system.sys in need_systems.keys():
                syscnt += 1
        if syscnt == 0:
            continue

        board_group = []

        board_cpu_t = SvgText(board.cpu, False)
        board_group.append(board_cpu_t)

        board_ip_t = SvgText(board.cpu_core, False)
        board_group.append(board_ip_t)

        board_prod_t = SvgText(board.product, False)
        board_group.append(board_prod_t)

        for sys in need_systems.keys():
            flag = False
            for system in board.systems:
                if system.sys != sys:
                    continue
                flag = True
                if len(system.variant) == 1:
                    sys_t = SvgText(str(system.variant[0].last_update), False)
                    # Use python's dynamic feature to add link without modifying the class
                    sys_t.link = system.variant[0].link
                    board_group.append(sys_t)
                    break
                var_g = []
                for var in system.variant:
                    sys_var = var.sys_var if var.sys_var is not None else "main"
                    sys_t = SvgText(sys_var + ': ' + str(var.last_update), False)
                    # Same as above
                    sys_t.link = var.link
                    var_g.append(sys_t)
                board_group.append(var_g)
                break
            if not flag:
                sys_t = SvgText("N/A", False)
                board_group.append(sys_t)
        table.append(board_group)

    col_width = [0] * len(head_row)
    for row in table:
        for idx, i in enumerate(row):
            if isinstance(i, list):
                for j in i:
                    col_width[idx] = max(col_width[idx], j.width())
            else:
                col_width[idx] = max(col_width[idx], i.width())

    row_height = [0] * len(table)
    for idx, row in enumerate(table):
        for i in row:
            if isinstance(i, list):
                row_height[idx] = max(row_height[idx],
                                      (conf.line_height() + conf.padding_y * 2) *
                                      len(i) + conf.stroke_width * (len(i) - 1))
            else:
                row_height[idx] = max(
                    row_height[idx], conf.line_height() + conf.padding_y * 2)

    doc = SvgXml()
    svg = SvgSvg()

    bg = SvgRectContainer('rgb(255, 128, 255)')

    top_border = SvgLine(
        sum(col_width) + conf.stroke_width * (len(col_width) + 3), 0,
        stroke_width=conf.stroke_width * 2)
    bg.add_child(top_border)
    bg.add_child(SvgCR())
    bg.add_child(SvgLF())

    # Head:
    head_bg = SvgRectContainer('rgb(200, 200, 200)')
    for idx, i in enumerate(table[0]):
        a = SvgAdvancer(conf.stroke_width * 2 if idx ==
                        0 else conf.stroke_width, 0)
        t = SvgTextCenter(i.text, col_width[idx], 0, True)
        g = SvgGroup()
        g.add_child(a)
        g.add_child(t)
        head_bg.add_child(g)
    head_bg.add_child(SvgCR())
    head_bg.add_child(SvgLF())

    bg.add_child(head_bg)
    bg.add_child(SvgCR())
    bg.add_child(SvgLF())

    # Now the data
    for rdx, row in enumerate(table[1:]):
        border = SvgLine(
            sum(col_width) + conf.stroke_width * (len(col_width) + 3), 0,
            stroke_width=conf.stroke_width)
        bg.add_child(border)
        bg.add_child(SvgCR())
        bg.add_child(SvgLF())

        row_g = SvgGroup()
        for idx, i in enumerate(row):

            a = SvgAdvancer(conf.stroke_width * 2 if idx ==
                            0 else conf.stroke_width, 0)
            g = SvgGroup()
            g.add_child(a)

            if isinstance(i, list):
                var_g = SvgGroup()

                for jdx, j in enumerate(i):

                    link = gen_link(None, None, j)
                    if link is not None:
                        t_lk = SvgLink(link)
                    else:
                        t_lk = SvgGroup()

                    t_bg = SvgRectContainer(gen_color(None, idx, j.text))
                    t = SvgTextCenter(j.text, col_width[idx], 0, False)

                    t_bg.add_child(t)
                    t_lk.add_child(t_bg)
                    var_g.add_child(t_lk)

                    if jdx < len(i) - 1:

                        a = SvgAdvancer(-t.width(), 0)
                        var_g.add_child(a)
                        var_g.add_child(SvgLF())

                        b = SvgLine(
                            t.width(), 0,
                            stroke_color='rgb(128,128,128)', stroke_width=conf.stroke_width)
                        var_g.add_child(b)

                        a = SvgAdvancer(-b.width(), 0)
                        var_g.add_child(a)
                        var_g.add_child(SvgLF())

                g.add_child(var_g)
            else:
                link = gen_link(None, None, i)

                if link is not None:
                    t_lk = SvgLink(link)
                else:
                    t_lk = SvgGroup()

                color = gen_color(None, idx, i.text)
                t_bg = SvgRectContainer(color)
                t = SvgTextCenter(
                    i.text, col_width[idx], row_height[rdx + 1], False)

                t_bg.add_child(t)
                t_lk.add_child(t_bg)
                g.add_child(t_lk)

            row_g.add_child(g)
        bg.add_child(row_g)
        bg.add_child(SvgCR())
        bg.add_child(SvgLF())

    # Bottom border
    bottom_border = SvgLine(
        sum(col_width) + conf.stroke_width * (len(col_width) + 3), 0,
        stroke_width=conf.stroke_width * 2)
    bg.add_child(bottom_border)

    # # Set the vertical lines
    svg_height = bg.height()
    bg.add_child(SvgMoveTo(0, 0))
    for idx, i in enumerate(col_width):
        bg.add_child(SvgLine(0, svg_height, stroke_width=conf.stroke_width *
                     2 if idx == 0 else conf.stroke_width))
        bg.add_child(SvgAdvancer(i, 0))
    bg.add_child(SvgLine(0, svg_height, stroke_width=conf.stroke_width * 2))

    svg.add_child(bg)
    doc.add_child(svg)

    return doc


def proc_onesys(system_arr: dict[str], system: Systems):
    """
    process one type of system
    """

    conf = SvgConf()

    res = gen_svg_table(conf, system, system_arr)

    return res


def main():
    """
    main
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', dest="path",
                        help="support matrix path", type=str, default='.')
    parser.add_argument('-o', '--output', dest="output",
                        help="output path", type=str, default='.')
    parser.add_argument('--html', dest="html",
                        help="output html, with svg assets at arg", type=str, default=None)

    args = parser.parse_args()

    p = args.path
    systems = Systems(p)

    html_path = args.html
    svg = proc_onesys(systems.linux, systems)
    with open(os.path.join(args.output, 'time-linux.svg'), 'w', encoding="utf-8") as f:
        f.write(str(svg))
    if html_path:
        with open(os.path.join(args.output, 'time-linux.html'), 'w', encoding="utf-8") as f:
            f.write(gen_html(svg, os.path.join(html_path, 'linux.svg')))
    svg = proc_onesys(systems.bsd, systems)
    with open(os.path.join(args.output, 'time-bsd.svg'), 'w', encoding="utf-8") as f:
        f.write(str(svg))
    if html_path:
        with open(os.path.join(args.output, 'time-bsd.html'), 'w', encoding="utf-8") as f:
            f.write(gen_html(svg, os.path.join(html_path, 'bsd.svg')))
    svg = proc_onesys(systems.rtos, systems)
    with open(os.path.join(args.output, 'time-rtos.svg'), 'w', encoding="utf-8") as f:
        f.write(str(svg))
    if html_path:
        with open(os.path.join(args.output, 'time-rtos.html'), 'w', encoding="utf-8") as f:
            f.write(gen_html(svg, os.path.join(html_path, 'rtos.svg')))
    svg = proc_onesys(systems.others, systems)
    with open(os.path.join(args.output, 'time-others.svg'), 'w', encoding="utf-8") as f:
        f.write(str(svg))
    if html_path:
        with open(os.path.join(args.output, 'time-others.html'), 'w', encoding="utf-8") as f:
            f.write(gen_html(svg, os.path.join(html_path, 'time-others.svg')))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Raise:", e)
        exit(1)
