<?php

namespace App;

use App\Enums\StatusEnum;
use Illuminate\Support\Carbon;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;

class Reservation
{
    /**
     * The code of the reservation.
     */
    private string $code;

    /**
     * The price of the reservation.
     */
    public StatusEnum $status;

    /**
     * Create a new Reservation instance.
     */
    public function __construct(
        private float $price,
        private Carbon $checkin,
        private Carbon $checkout,
        private float $discount = 0,
    ) {
        $this->code = Str::uuid();

        $this->status = StatusEnum::PENDING;
    }

    /**
     * Get the price of the reservation.
     */
    public function getPrice(): float
    {
        return $this->price - $this->discount;
    }

    /**
     * Get the status of the reservation.
     */
    public function getStatus(): StatusEnum
    {
        return $this->status;
    }

    /**
     * Get the code of the reservation.
     */
    public function getCode(): string
    {
        return $this->code;
    }

    /**
     * Get the checkin date of the reservation.
     */
    public function getCheckin(): Carbon
    {
        return $this->checkin;
    }

    /**
     * Get the checkout date of the reservation.
     */
    public function getCheckout(): Carbon
    {
        return $this->checkout;
    }

    /**
     * Set the status of the reservation.
     *
     * Does this make sense?
     */
    public function setStatus(StatusEnum $status): void
    {
        $this->status = $status;
    }

    /**
     * Save the reservation on the database.
     */
    public function save(): void
    {
        DB::table('reservations')->insert([
            'code' => $this->code,
            'price' => $this->price,
            'status' => $this->status,
            'checkin' => $this->checkin,
            'checkout' => $this->checkout,
            'discount' => $this->discount,
        ]);
    }
}
