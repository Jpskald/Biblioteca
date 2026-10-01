const CACHE_NAME = 'biblioteca-cache-v1';
// Lista de recursos para salvar no celular do usuário
const urlsToCache = [
  '/',
  '/static/manifest.json',
  'https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Retorna do cache se encontrar, senão vai para a internet
        return response || fetch(event.request);
      })
  );
});
