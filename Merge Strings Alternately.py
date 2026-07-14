class Solution(object):

  # In above step we have created a class with the object  
    def mergeAlternately(self, word1, word2):

      # Created a function 

      # self , word1, word 2 are the parameter we are passing through the function
        m = len(word1)

      # m is an variable which holds the leght of word1
        n = len(word2)

            # n is an variable which holds the leght of word2

        i = 0

      # we have created a variable and initialized thevalue to 0
        j = 0

      # created a variable and initialized the value to 0
        result = []
        # created a array _r where we are storing the data in it
        while i < m or j < n:

          # initiated a while loo

          # where as the loop runs untill 

          # It satisfys the condition i < m or j < n  

        # where as it have to satisfy atleast one condition to run the  loop
            if i < m:

              # we have use if condition 

              # where as the the condition  i < m 

              # The condition to be satisfied to run the internal block of the code
                result += word1[i]

              # if the condition is satisfied

              # the element i is going to be added in word1
                i += 1

          # then after it continues untill the condition is breaked


          #  until  the value of i increases
            if j < n:


              # we have created another internal condition


              # condition j< n
                result += word2[j]

              # if the condition is satisfied the element j is inseted into the word2

              
                j += 1
            # After every successfull iteration the value of j is increamented further


      # the condition iterates untill the condition breaks
      
        return "".join(result)
  # the join() fubction prints the elements in the result[] array 

  # without any external items in it


