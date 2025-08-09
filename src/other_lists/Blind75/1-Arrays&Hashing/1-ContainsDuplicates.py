class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # using hashset -> only care about duplicates, and no order
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

        # Using hashmap -> unnessary of saving idx in this problem
        hm = {}
        for idx, num in enumerate(nums):
            if num in hm:
                return True
            else:
                hm[num] = idx
        return False


""" NOTES:

List are mutable .i.e it can be converted into another data type and can store any data element in it.
List can store any type of element.

ways to create a list:
list1=[1,4,"Gitam",6,"college"]
list2=[]  # creates an empty list
list3=list((1,2,3))


"""