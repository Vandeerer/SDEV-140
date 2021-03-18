print("Midterm by Taylor Griffin")
sentence=[]
sentence = input('Input a Sentence: ').strip().split()
sentence[0] = sentence[0][0].upper() + sentence[0][1:]
if "." not in sentence[len(sentence)-1]:
      sentence[len(sentence)-1] += "."
for temp in range(len(sentence)):
      if temp != len(sentence)-1:
            print(sentence[temp] ,end = " ")
      else:
            print(sentence[temp])
print("There are",len(sentence),"words in the sentence.")
