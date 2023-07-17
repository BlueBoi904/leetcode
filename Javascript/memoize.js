function memoize(fn) {
    var cache = {};

    return function (...args) {
        let key = String(args);

        if (key in cache) return cache[key];
        return cache[key] = fn(...args);
    }
}