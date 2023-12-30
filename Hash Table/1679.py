class Solution(object):
    def maxOperations(self, nums, k):
        my_dict, count = {}, 0
        for i in nums:
            if i < k:
                if not (i in my_dict):
                    if (k-i) in my_dict:
                        my_dict[k-i] += 1
                    else:
                        my_dict[k-i] = 1
                else:
                    count += 1
                    my_dict[i] -= 1
                    if my_dict[i] == 0:
                        my_dict.pop(i)
        return count

        # return (lambda c: sum(min(c[n], c[k-n]) for n in c))(Counter(nums))//2