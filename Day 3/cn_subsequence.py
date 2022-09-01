Problem link : https://www.codingninjas.com/codestudio/problems/subsequences-of-string_985087?leftPanelTab=0
    
Code :

def solve(str,output,index,ans):
    if(index >= len(str)):
        if len(output) > 0:
            ans.append(output)
        return 
    solve(str,output,index+1,ans)
    x = str[index]
    output = output + (x)
    solve(str,output, index+ 1, ans)


def subsequences(str):
    ans = []
    output = ""
    index = 0
    solve(str,output,index,ans)
    return ans
   
    pass
