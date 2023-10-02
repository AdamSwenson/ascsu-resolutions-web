<?php

namespace App\Exceptions;

use Exception;
use Throwable;

/**
 * Thrown whenever there is an error in a python script.
 * Message contains the error output.
 */
class PythonScriptError extends Exception
{
    //

    public function __construct(string $message = "", int $code = 0, ?Throwable $previous = null)
    {
        parent::__construct($message, $code, $previous);
    }
}
