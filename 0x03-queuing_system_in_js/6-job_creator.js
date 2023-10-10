const kue = require('kue');
const queue = kue.createQueue();

const job = queue.create('push_notification_code', {
    phoneNumber: '0786559151',
    message: 'pending'
}).save(() => {
    console.log(`Notification job created: ${job.id}`)
});

job.on('complete', () => {
    console.log(`Notification job completed`);
}).on('failed', () => {
    console.log('Notification job failed')
})