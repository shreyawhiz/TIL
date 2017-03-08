`Gulp`

gulp is a toolkit that helps you automate painful or time-consuming tasks in your development workflow.


`gulp silent`
	Options to make the default gulp messages off
	
	// Run the project in silent mode
	gulp.task('silent', function (done) {
    		runSequence('env:dev', ['copyLocalEnvConfig'], ['nodemon', 'watch'], done);
	});
	
	
You can resolve `EOSPC` error with the help of the following command


`echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p`

The system has a limit to how many files can be watched by a user. 
You can run out of watches pretty quickly if you have Grunt running with other programs like Dropbox. 
This command increases the maximum amount of watches a user can have.
