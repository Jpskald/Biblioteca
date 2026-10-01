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

importScripts('https://cdnjs.cloudflare.com/ajax/libs/localforage/1.10.0/localforage.min.js');

self.addEventListener('sync', event => {
  if (event.tag === 'sync-leitores') {
    console.log("Internet voltou! Sincronizando dados pendentes...");
    event.waitUntil(enviarDadosPendentes());
  }
});

function enviarDadosPendentes() {
  return localforage.getItem('fila_leitores').then(fila => {
    if (!fila || fila.length === 0) return;

    // Envia cada item da fila para a API do Django
    let promessas = fila.map(dados => {
      return fetch('/api/leitor/criar/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(dados)
      });
    });

    // Se tudo for enviado com sucesso, limpa a fila do IndexedDB
    return Promise.all(promessas).then(() => {
      console.log("Sincronização concluída com sucesso!");
      return localforage.removeItem('fila_leitores');
    });
  });
}
