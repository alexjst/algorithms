package alexyang.algorithms.Java.LinkedIn;

import alexyang.algorithms.Java.LinkedIn.*;
import java.io.*;
import java.util.*;

public class RetainBestCache<K, V extends Rankable> {
    // Add any fields you need here
    public static class KV<K,V> {
        K k;
        V v;
        public KV (K k, V v) {
            this.k = k;
            this.v = v;
        }

        @Override
        public boolean equals(Object o) {
            if (o == this) {
                return true;
            }

            if (!(o instanceof KV)) {
                return false;
            }

            KV c = (KV) o;
            return c.k.equals(this.k) && c.v.equals(this.v);
        }
    }

    DataSource<K,V> ds;
    int capacity;

    Map<K,V> map;
    Set<KV> set;

    /* Constructor with a data source (assumed to be slow) and a cache size */
    public RetainBestCache(DataSource<K, V> ds, int maxEntries) {
        // Implementation here
        if (ds==null || maxEntries <= 0) {
            throw new IllegalArgumentException("Invalid argument creating cache.");
        }
        this.ds = ds;
        this.capacity = maxEntries;
        map = new HashMap<>();

        set = new TreeSet<KV> (new Comparator<KV>() {
            public int compare(KV kv1, KV kv2) {
                long r1 = kv1.v.getRank();
                long r2 = kv2.v.getRank();
                if (r1 != r2) {
                    return (int)(r1 - r2);
                } else {
                    return kv1.hashCode() - kv2.hashCode();
                }
            }
        });
    }

    /* Gets some data. If possible, retrieves it from cache to be fast. If the data is not cached,
     * retrieves it from the data source. If the cache is full, attempt to cache the returned data,
     * evicting the V with lowest rank among the ones that it has available
     * If there is a tie, the cache may choose any T with lowest rank to evict.
     */
    public V get(K key) {
        // Implementation here
        if (map.containsKey(key)) { // O(1)
            return map.get(key);
        } else { // O(log(N))
            V val = ds.get(key);
            add(key,val);
            return val;
        }
    }

    // add <K,V> and possibly evict
    private void add(K k, V v) {
        if (map.containsKey(k)) {
            set.remove(new KV(k, map.get(k)));
        }
        set.add(new KV(k,v));
        map.put(k,v);
        if (map.size() > capacity) {
            KV kv = set.iterator().next();
            set.remove(kv);
            map.remove(kv.k);
        }
    }
}
