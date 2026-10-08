class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        import heapq

        frequencies = {}
        heap = []

        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        for num, frequency in frequencies.items():
            heapq.heappush(heap, (frequency, num))
            if len(heap) > k:
                heapq.heappop(heap)
                
        answer = [num for freq, num in heap]
        return answer
