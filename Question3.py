############## find Anagram word of paragraph
from collections import defaultdict  
  
def find_anagram(words): 
    groupedWords = defaultdict(list) 
   
    for word in words: 
        groupedWords["".join(sorted(word))].append(word) 
      
    print("The word and it's anagram : ")
    for group in groupedWords.values(): 
        print(" ".join(group))       
 
if __name__ == "__main__":    
    paragraph =input("Enter your paragraph : ").split()   
    find_anagram(paragraph)      
