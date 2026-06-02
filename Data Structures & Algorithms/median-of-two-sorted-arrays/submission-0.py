class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total_len = len(A) + len(B)
        half = total_len // 2 # is the index of median

        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            mid_A = (l + r) // 2
            idx_B = half - mid_A - 2

            Aleft = A[mid_A] if mid_A >= 0 else float('-inf')
            Aright = A[mid_A + 1] if mid_A + 1 < len(A) else float('inf')
            Bleft = B[idx_B] if idx_B >= 0 else float('-inf')
            Bright = B[idx_B + 1] if idx_B + 1 < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total_len % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = mid_A - 1
            else:
                l = mid_A + 1
