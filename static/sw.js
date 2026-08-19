// RiceGuard AI - Progressive Web App Service Worker
const CACHE_NAME = 'riceguard-pwa-v1';
const STATIC_ASSETS = [
    '/',
    '/static/manifest.json',
    '/static/icons/icon-192.png',
    '/static/icons/icon-512.png',
    '/static/samples/brown_spot.jpg',
    '/static/samples/healthy.jpg',
    '/static/samples/leaf_blast.jpg',
    '/static/samples/bacterial_blight.jpg'
];

// Install Event - Pre-cache core shell
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(STATIC_ASSETS);
        }).then(() => self.skipWaiting())
    );
});

// Activate Event - Clean up outdated caches
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((keys) => {
            return Promise.all(
                keys.map((key) => {
                    if (key !== CACHE_NAME) {
                        return caches.delete(key);
                    }
                })
            );
        }).then(() => self.clients.claim())
    );
});

// Fetch Event - Stale-while-revalidate for static, Network-first for POST/API
self.addEventListener('fetch', (event) => {
    const req = event.request;
    const url = new URL(req.url);

    // Only handle GET requests
    if (req.method !== 'GET') {
        return;
    }

    // Static assets & images: Cache First with network fallback
    if (url.pathname.startsWith('/static/') || url.pathname.includes('fonts.googleapis.com') || url.pathname.includes('fonts.gstatic.com')) {
        event.respondWith(
            caches.match(req).then((cachedResp) => {
                if (cachedResp) {
                    return cachedResp;
                }
                return fetch(req).then((networkResp) => {
                    if (networkResp.status === 200) {
                        const respClone = networkResp.clone();
                        caches.open(CACHE_NAME).then((cache) => cache.put(req, respClone));
                    }
                    return networkResp;
                });
            })
        );
        return;
    }

    // HTML Pages: Network first with Cache fallback
    event.respondWith(
        fetch(req).then((networkResp) => {
            if (networkResp.status === 200) {
                const respClone = networkResp.clone();
                caches.open(CACHE_NAME).then((cache) => cache.put(req, respClone));
            }
            return networkResp;
        }).catch(() => {
            return caches.match(req).then((cachedResp) => {
                if (cachedResp) return cachedResp;
                if (req.headers.get('accept').includes('text/html')) {
                    return caches.match('/');
                }
            });
        })
    );
});
