class Solution(object):
    def permute(self, nums):
        if len(nums)==1:
            return [nums[:]]

        res=[]

        for _ in range(len(nums)):

            n= nums.pop(0)

            perms= self.permute(nums)


            for p in perms:
                p.append(n)

            res.extend(perms)
            nums.append(n)

        return res
            

        