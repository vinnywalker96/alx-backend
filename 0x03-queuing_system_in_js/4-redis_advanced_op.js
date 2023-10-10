import { RedisClient, createClient, print } from 'redis';

const client = createClient();

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

client.on('error', function (err) {
  console.log(`Redis client not connected to the server: ${err}`);
});

const hashKey = "HolbertonSchools";
const data = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2
};

for (const key in data){
    client.hset('HolbertonSchools', key, data[key]);
}

let schools = client.hgetall('HolbertonSchools', (err, reply) => {
    if (err){
        console.log(err);
    } else {
        console.log(reply)
    }

});




