import http from 'k6/http';
import { sleep, check } from 'k6';

export let options = {
    stages: [
        { duration: '1s', target: 100 },  // Simulate ramp-up of traffic from 0 to 100 users over 1 second.
        { duration: '8s', target: 100 },  // Stay at 100 users for 8 seconds.
        { duration: '1s', target: 0 },    // Ramp-down to 0 users over 1 second.
    ],
};

export default function () {
    let url = 'https://ms1.productbrand.localhost/api/v1/product_brand/create';
    let payload = JSON.stringify({
        id_client: Math.random().toString(36).substring(2, 15),
        id_product: 'asdas',
        payment_method: 'asdsdaasdasd',
        total: (Math.random() * 100).toFixed(2)
    });

    let params = {
        headers: {
            'Content-Type': 'application/json',
        },
    };

    let res = http.post(url, payload, params);

    check(res, {
        'is status 200': (r) => r.status === 200,
        'response time < 500ms': (r) => r.timings.duration < 500,
    });

    sleep(0.1); // Adjust sleep to increase the number of requests per user
}