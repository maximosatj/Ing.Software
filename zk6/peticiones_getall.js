import http from 'k6/http';
import { check, sleep } from 'k6';

const rate = 1000; // Peticiones por segundo

export let options = {
  insecureSkipTLSVerify: true, // Habilitar el modo insecure
  scenarios: {
    constant_request_rate: {
      executor: 'constant-arrival-rate',
      rate: rate, // Peticiones por segundo
      timeUnit: '1s', // Cada segundo
      duration: '10s', // Duración del test
      preAllocatedVUs: 50, // Usuarios virtuales preasignados
      maxVUs: 100, // Máximo de usuarios virtuales
    },
  },
};

// URL que se quiere testear
const url = 'https://ms1.productbrand.localhost/api/v1';
// const url = 'http://127.0.0.1:5000/api/v1/';

export default function () {
  let res = http.get(url);
  check(res, {
    'status was 200': (r) => r.status === 200,
  });
  sleep(1);
}