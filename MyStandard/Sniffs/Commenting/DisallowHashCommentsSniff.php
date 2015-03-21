<?php
/**
 * This sniff prohibits the use of Perl style hash comments.
 *
 * PHP version 5
 *
 * @category  PHP
 * @package   PHP_CodeSniffer
 * @author    Your Name <you@domain.net>
 * @license   https://github.com/squizlabs/PHP_CodeSniffer/blob/master/licence.txt BSD Licence
 * @link      http://pear.php.net/package/PHP_CodeSniffer
 */

/**
 * This sniff prohibits the use of Perl style hash comments.
 *
 * An example of a hash comment is:
 *
 * <code>
 *  # This is a hash comment, which is prohibited.
 *  $hello = 'hello';
 * </code>
 * 
 * @category  PHP
 * @package   PHP_CodeSniffer
 * @author    Your Name <you@domain.net>
 * @license   https://github.com/squizlabs/PHP_CodeSniffer/blob/master/licence.txt BSD Licence
 * @version   Release: @package_version@
 * @link      http://pear.php.net/package/PHP_CodeSniffer
 */
class MyStandard_Sniffs_Commenting_DisallowHashCommentsSniff implements PHP_CodeSniffer_Sniff
{

  /**
	 * A list of tokenizers this sniff supports.
	 *
	 * @var array
	 */
	public $supportedTokenizers = array(
	  'PHP',
    'JS',
  );

  /**
   * Register the token that sniff is interested in
   *
   * @return array(int)
   */
  public function register()
  {
    return array(T_COMMENT);
  }

  /**
   * Actual processing once interested token is encoutered
   *
   * @param PHP_CodeSniffer_File $phpcsFile The file where the token was found.
   * @param int                  $stackPtr  The position in the stack where
   *                                        the token was found.
   *
   * @return void
   */
  public function process(PHP_CodeSniffer_File $phpcsFile, $stackPtr)
  {
    $tokens = $phpcsFile->getTokens();
    if ($tokens[$stackPtr]['content'][0] == '#') {
      $error = 'Hash comments are prohibited; found %s';
      $data  = array(trim($tokens[$stackPtr]['content']));
      $phpcsFile->addError($error, $stackPtr, 'Found', $data);
    }
  }

}
