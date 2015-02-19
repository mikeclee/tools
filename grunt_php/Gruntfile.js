/**
 * Grunt main configuration file
 */
module.exports = function(grunt) {
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		phplint: {
			options: {
				// phpCmd: '/usr/bin/php',
				phpArgs: {
					"-l": null
				},
				// spawnPath: '/tmp', // Default os.tmpDir()
				spawnLimit: 10
			},
			good: ['src/php/good.php'],
			bad: ['src/php/bad.php']
		},
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

	grunt.loadNpmTasks('grunt-phplint');
	grunt.loadNpmTasks('grunt-contrib-uglify');

	//grunt.loadTasks('./tasks');
	//grunt.registerTask('default', ['uglify']);
};
