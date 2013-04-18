<?php

/**
 * User Model
 *
 * PHP Version 5
 *
 * @category Controllers
 * @package  Tesla
 * @author   David Francos Cuartero <me@davidfrancos.net>
 * @license  GPL2+ <http://foo.car>
 * @link     http://lcdv.com/
 */
/**
 * User
 *
 * @uses Eloquent
 * @category Controllers
 * @package  Tesla
 * @author   David Francos Cuartero <me@davidfrancos.net>
 * @license  GPL2+ <http://foo.car>
 * @link     http://lcdv.com/
 */
class User extends Eloquent
{
    public static $hidden = array('password');
}
