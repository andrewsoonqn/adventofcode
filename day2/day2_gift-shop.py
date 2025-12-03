from typing import Iterator

class Solution:
    def _stream_product_ids(self, filepath: str) -> Iterator[tuple[int, int]]:
        with open(filepath) as f:
            for id_range in iter(f.read().split(',')):
                yield int(id_range.split('-')[0]), int(id_range.split('-')[1])

    def invalid_ids(self, filepath: str) -> int:
        # sum of invalid ids
        invalid_ids = 0

        for s, e in self._stream_product_ids(filepath):
            # print(f"{s}-{e}")
            for i in range(s, e+1):
                strand = str(i)
                if len(strand) % 2 != 0:
                    continue
                else:
                    left = strand[:len(strand)//2]
                    right = strand[len(strand)//2:]
                    if left == right:
                        invalid_ids += i

        return invalid_ids

print(Solution().invalid_ids("input"))