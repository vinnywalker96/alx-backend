const kue = require('kue');
const queue = kue.createQueue();
const blacklistedNumbers = ['4153518780', '4153518781'];


function sendNotification(phoneNumber, message, job, done) {
    console.log(`Notification job #${job.id} 0% complete`);

    job.progress(0, 100); 

    if (blacklistedNumbers.includes(phoneNumber)) {
        const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
        console.log(`Notification job #${job.id} failed: ${errorMessage}`);
        return done(new Error(errorMessage));
    }

    job.progress(50, 100);
    console.log(`Notification job #${job.id} 50% complete`);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    setTimeout(() => {
        job.progress(100, 100);
        console.log(`Notification job ${job.id} completed`);
        done(); 
    }, 1000);
}
const queueName = 'push_notification_code_2';
const concurrency = 2; 
queue.process(queueName, concurrency, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});

console.log(`Job processor for queue ${queueName} is running.`);
