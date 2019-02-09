# Question: Write an algorithm to determine whether two strings are anagrams or not.
# An anagram is a word or phrase formed by rearranging the letters in another word or phrase.

# abcd - > dbca TRUE
# abc - /  abd FALSE
# acc ->  ccaa FALSE

# Find all anagrams of a given word. A dictionary including all English words is provided.

def anagram(str, strTwo):
  
  mapOne = {}
  
  if len(str) != len(strTwo):
    return False
  
  for i in str:
    if i in mapOne.keys():
      mapOne[i] += 1
      continue
    
    mapOne[i] = 1
    

  for i in strTwo:
    # check if i in map, occurances
    
    if i not in mapOne.keys():
        return False
    
    mapOne[i] -= 1
    
    if mapOne[i] < 0:
      return False
  
  return True


# print(anagram("abc", "abc"))
print(anagram("abc", "abd"))


# Anagram basic

# Anagram faster

# Anagram faster

# Dictionary anagram system design preprocessing 







































# Question: Write an algorithm to determine whether two strings are anagrams or not.
# An anagram is a word or phrase formed by rearranging the letters in another word or phrase.

# abcd - > dbca TRUE
# abc - /  abd FALSE
# accc -> accb FALSE

# Find all anagrams of a given word. A dictionary including all English words is provided.

public static List<String> getAnagrams(String str, Set<String> dictionary){
    List<String> anagrams = new ArrayList<>();
    int strHash = getHash(str);

    for(String s: dictionary){
        if(strHash == getHash(s)){
            anagrams.add(s);
        }
    }

    return anagrams;
}

public static int getHash(String str) {
    int[] primes =  {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101};

    int hash = 1;
    for(int i = 0; i < str.length(); i++){
        hash *= primes[str.charAt(i)-'a'];
    }
    return hash;
}

# abc > 2* 3 * 5 = 30
# abb > 18

# def anagram(str, strTwo):

#   mapOne = {}
  
#   if length(str) != len(strTwo):
#     return False
  
#   for i in str:
#     if i in mapOne.keys():
#       mapOne.i += 1
#       continue
    
#     mapOne.add(i)
#     mapOne.i = 1
    
  
#   for i in strTwo:
#     # check if i in map, occurances
#     if i not in map.keys():
#         return False
    
#     mapOne.i -= 1
    
#     if map.i < 0:
#       return False
  
#   return True


# print(anagram("abcd", "dbca"))
# print(anagram("abc", "abd"))























