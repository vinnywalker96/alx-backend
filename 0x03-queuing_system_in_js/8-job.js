import kue from 'kue';
const q = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }
    for (const jobData of jobs) {
        const job = queue.create('push_notification_code_3', jobData)
            .save((err) => {
                if (err) {
                    console.error(`Error creating job: ${err.message}`);
                } else {
                    console.log(`Notification job created: ${job.id}`);

                    job.on('complete', function () {
                        console.log(`Notification job ${job.id} completed`);
                    })
                    job.on('failed', function (errorMessage)  {
                        console.error(`Notification job ${job.id} failed: ${errorMessage}`);
                    })
                    job.on('progress', function(progress, data){
                        console.log(`Notification job ${job.id} ${progress}% complete`);
                    })
                
            }
            });

           
    };
}

module.exports = createPushNotificationsJobs;
