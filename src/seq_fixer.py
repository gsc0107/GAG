#!/usr/bin/env python


class SeqFixer:

    def __init__(self):
        self.terminal_ns = False
        self.internal_stops = False
        self.start_stop_codons = False

    def fix(self, seq):
        if self.terminal_ns:
            # TODO implement method on sequence first
            pass
        if self.internal_stops:
            # TODO implement method on sequence first
            pass
        if self.start_stop_codons:
            seq.create_starts_and_stops()

