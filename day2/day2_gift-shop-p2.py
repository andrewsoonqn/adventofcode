from typing import Iterator

class Solution:
    def _stream_product_ids(self, filepath: str) -> Iterator[tuple[int, int]]:
        with open(filepath) as f:
            for id_range in iter(f.read().split(',')):
                yield int(id_range.split('-')[0]), int(id_range.split('-')[1])

    def is_invalid(self, id: int) -> bool:
        strand = str(id)
        n = len(strand)

        for i in range(1, n // 2 + 1):

            # Optimisation
            if n % i != 0:
                continue

            pattern = strand[:i]
            match = True

            # Check sequential blocks of size `i` starting from `i`
            for ptr in range(i, n, i):
                if strand[ptr:ptr + i] != pattern:
                    match = False
                    break

            if match:
                return True

        return False


    def invalid_ids(self, filepath: str) -> int:
        # Sum of invalid ids
        invalid_ids = 0

        for s, e in self._stream_product_ids(filepath):
            # print(f"{s}-{e}")
            for i in range(s, e+1):
                if self.is_invalid(i):
                    invalid_ids += i

        return invalid_ids

print(Solution().invalid_ids("input"))