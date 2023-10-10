import { expect } from "chai";
import kue from 'kue';

import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

const list = [
    {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
    }
];


before(function(){
    queue.testMode.enter(true);
});

afterEach(function (){
    queue.testMode.clear();
});

after(function (){
    queue.testMode.exit();
});

it('Should validate which jobs are inside the queue', () => {
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    // expect(queue.testMode.data).to.eq(list[0]);
});

it('Should validate active jobs', () => {
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs[0].data).to.eql(
        {
            phoneNumber: '4153518780',
            message: 'This is the code 1234 to verify your account'
        }
        
    );
});
