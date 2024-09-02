<?php

namespace App\Abstracts;

abstract class Action
{
    /**
     * Execute the action instance.
     */
    public static function execute(...$arguments)
    {
        return (new static(...$arguments))->handle();
    }

    /**
     * Execute the action with the given arguments if the given truth test passes.
     */
    public static function executeIf(bool $boolean, ...$arguments)
    {
        if ($boolean) {
            return (new static(...$arguments))->handle();
        }
    }

    /**
     * Execute the action with the given arguments unless the given truth test passes.
     */
    public static function executeUnless(bool $boolean, ...$arguments)
    {
        if (! $boolean) {
            return (new static(...$arguments))->handle();
        }
    }

    /**
     * Execute the action.
     */
    abstract protected function handle();
}
