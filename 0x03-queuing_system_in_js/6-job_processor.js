const kue = require('kue');
const queue = kue.createQueue();

function sendNotification(phoneNumber, message){
    const job = queue.create('push_notification_code',{
        phoneNumber: phoneNumber,
        message: message
    }).save(() => {
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    });

    job.on('complete', () => {
        console.log(`Notification job completed`);
    }).on('failed', () => {
        console.log('Notification job failed')
    })
} 

sendNotification('4153518780', 'This is the code to verify your account');