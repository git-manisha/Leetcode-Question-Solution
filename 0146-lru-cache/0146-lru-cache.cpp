class LRUCache {
public:
    list<int> dll;
    map<int,pair<list<int>::iterator,int>> mp;
    int size;
    LRUCache(int capacity) {
        size = capacity;
    }
    void makeRecentUsed(int key){
        dll.erase(mp[key].first);

        dll.push_front(key);
        mp[key].first = dll.begin();
    }
    int get(int key) {
        if(mp.find(key) == mp.end()){
            return -1;
        }

        makeRecentUsed(key);

        return mp[key].second;
    }
    
    void put(int key, int value) {
        
        if(mp.find(key) != mp.end()){
            mp[key].second = value;
            makeRecentUsed(key);
        }
        else{
            dll.push_front(key);
            mp[key] = {dll.begin(),value};
            size--;
        }
        if(size <0){
            int key_tobe_del = dll.back();
            mp.erase(key_tobe_del);

            dll.pop_back();
            size++;
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */