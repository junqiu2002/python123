def Check_Vow(string, vowels):
    final = [curChar for curChar in string if curChar in vowels]
    print(len(final))
    print(final)
     
# Driver Code
string = "Geeks for Geeks"
vowels = "AaEeIiOoUu"
Check_Vow(string, vowels);
