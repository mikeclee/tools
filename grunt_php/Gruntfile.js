/**
 * Grunt main configuration file
 */
module.exports = function(grunt) {
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		uglify: {
			options: {
				banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n',
				preserveComments: false
			},
			build: {
				src: 'src/js/test.js',
				dest: 'build/js/package.min.js'
			}
		}
	});

	grunt.loadNpmTasks('grunt-contrib-uglify');

	//grunt.registerTask('default', ['uglify']);
};
