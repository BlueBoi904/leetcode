# start & end of sliding window: |start-> ... end->|

# short version of sliding window, focus on two pointers


def start_end_sliding_window(self, seq):
    start, end = 0, 0

    while end < len(seq):
        # end pointer grows in the outer loop

        end += 1

        # start pointer grows with some restrict

        while self.start_condition(start):
            # process logic before pointers movement

            self.process_logic1(start, end)

            # start grows in the inner loop

            start += 1

        # or process logic after pointers movement

        self.process_logic2(start, end)
