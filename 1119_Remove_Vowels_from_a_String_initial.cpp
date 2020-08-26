class Solution {
public:
    string removeVowels(string S) {
        
        string result;
        int length = S.length();
        set<char> store;
        store = {'a','e','i','o','u'};
        // tested .
        
        for(int i = 0; i<length; i++){
            
            auto index = store.find(S[i]);
            if(index == store.end()){
                
                result.push_back(S[i]);
            }else{
                
                // Do nothing
            }
        }
    
        
        return result;
    }
};
