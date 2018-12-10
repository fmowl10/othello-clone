import curses

from logic.board import Board
from logic.enums import Status

# check ~/test_mouse.py


def main_game():
    stdscr = curses.initscr()
    stdscr.border()
    curses.curs_set(0)
    curses.mousemask(1)
    stdscr.refresh()
    win = curses.newwin(11, 11, 1, 1)
    stdscr.keypad(1)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    win.border()
    win.refresh()
    board = Board(8)
    board.start_game()
    stdscr.refresh()
    try:
        while True:
            event = stdscr.getch()
            win.border()
            win.refresh()
            if event == curses.KEY_MOUSE:
                _, mx, my, _, _ = curses.getmouse()
                if 14 <= mx <= 16 and my == 8:
                    print(board, file=board.f)
                    curses.endwin()
                    board.f.close()
                    break
                stdscr.clear()
                stdscr.border()
                stdscr.addstr(8, 14, 'end', curses.color_pair(1))
                
                stdscr.addstr(20, 1, '                 ', curses.color_pair(1))
                stdscr.addstr(
                    20, 20, str((mx - 3, my - 3)), curses.color_pair(1)
                )
                stdscr.refresh()
                if 2 <= mx <= 10 and 2 <= my <= 10:
                    output = board.place_cell(my - 3, mx - 3)
                    stdscr.addstr(
                        22, 20, output, curses.color_pair(1)
                    )
                    is_over = board.next_turn()
                    if output in ['pass', 'right'] and not is_over:
                        stdscr.addstr(
                            9, 14, str(board.turn), curses.color_pair(1))
                        if board.get_is_pass():
                            board.next_turn()
                    if output == 'game over' or board.is_over:
                        winner = ''
                        if board.who_win == Status.WHITE:
                            winner = 'White'
                        else:
                            winner = 'Black'
                        stdscr.addstr(
                            9, 14, winner, curses.color_pair(1)
                        )
                    stdscr.refresh()
                    win.refresh()
            for i in range(9):
                if i < 1:
                    continue
                win.border()
                win.addstr(
                    1, i + 1, chr(ord('a') + i - 1), curses.color_pair(1))
                win.addstr(i + 1, 1, str(i), curses.color_pair(1))
                for i, v in enumerate(str(board).split('\n')):
                    win.addstr(i + 2, 2, v)
                win.refresh()
    except Exception as e:
        raise e
        print(e, file=board.f)
    finally:
        board.f.close()
        curses.endwin()


if __name__ == '__main__':
    main_game()
