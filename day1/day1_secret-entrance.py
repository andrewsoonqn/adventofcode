import re
from typing import Iterator, Tuple

class Solution:
    def __init__(self):
        self._pattern = re.compile(r"([LR])(\d+)", re.IGNORECASE)

    def _stream_instructions(self, filepath: str) -> Iterator[Tuple[str, int]]:
        with open(filepath) as f:
            for line in f:
                for match in self._pattern.finditer(line):
                    yield match.group(1), int(match.group(2))
    def find_password(self, filepath: str):
        password = 0
        pos = 50

        for direction, amt in self._stream_instructions(filepath):
            if direction.upper() == 'L':
                amt = -amt

            pos = (pos + amt) % 100

            if pos == 0:
                password += 1

        return password

print(Solution().find_password("input"))





