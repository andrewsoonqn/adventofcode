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
            prev_pos = pos

            print(f"{direction} {amt}")
            if direction.upper() == 'L':
                amt = -amt

            pos += amt
            print(f"shifted to {pos}")

            if direction.upper() == 'L':
                clicks = (prev_pos - 1) // 100 - (pos - 1) // 100
            else:
                clicks = pos // 100 - prev_pos // 100

            password += clicks
            print(f"password = {password}")

        return password

print(Solution().find_password("input"))





