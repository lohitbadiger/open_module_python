def fis():
    
    input_file=open('L:\program\interview_task\solution\\input_file.txt','r')
    read_text=input_file.read()
    import string 
    
    data={}

    # using sum() + strip() + split() 
    # to count words in string 
    res = sum([i.strip(string.punctuation).isalpha() for i in read_text.lower().split()]) 
    
    # printing result 
    res= ("Total word count: " +  str(res)) 

    data['res']=res


    count = {}
    for w in open('L:\program\interview_task\solution\\input_file.txt').read().lower().split():
        if w in count:
            count[w] += 1
        else:
            count[w] = 1
    count=len(count)

    count='\ntotal unique words '+str(count)
    data['count']=count

    # print(' The top 10 words based on their word count, showing the word and how many times it appeared.')
    

    output_file=open('wc_report.txt','w')
    output_file.write(data['res'])
    output_file.write(data['count'])
    
    word_counter = {}
    for word in read_text.lower().split(" "): # split in every space.
        if len(word) > 0 and word.lower().strip(string.punctuation).isalpha():
            if word not in word_counter: # if 'word' not in word_counter, add it, and set value to 1
                word_counter[word] = 1
            else:
                word_counter[word] += 1 # if 'word' already in word_counter, increment it by 1

    for i,word in enumerate(sorted(word_counter,key=word_counter.get,reverse=True)[:10]):
        # sorts the dict by the values, from top to botton, takes the 10 top items,
        output_file.write("\n %s: %s - %s\n"%(i+1,word,word_counter[word]))
        
    input_file.close()

    

fis()