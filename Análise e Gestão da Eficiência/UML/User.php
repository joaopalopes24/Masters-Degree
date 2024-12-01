<?php

namespace App;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Hash;

class User
{
    /**
     * The name of the user.
     */
    private string $name;

    /**
     * The password of the user.
     */
    private string $password;

    /**
     * Create a new User instance.
     */
    public function __construct(
        public string $email,
    ) {}

    /**
     * Get the name of the user.
     */
    public function getName(): string
    {
        return $this->name;
    }

    /**
     * Set the name of the user.
     */
    public function setName(string $firstName, string $lastName): void
    {
        $this->name = "{$firstName} {$lastName}";
    }

    /**
     * Set the password of the user.
     */
    public function setPassword(string $password): void
    {
        $this->password = Hash::make($password);
    }

    /**
     * Save the user on the database.
     */
    public function save(): void
    {
        DB::table('users')->insert([
            'name' => $this->name,
            'email' => $this->email,
            'password' => $this->password,
        ]);
    }
}
