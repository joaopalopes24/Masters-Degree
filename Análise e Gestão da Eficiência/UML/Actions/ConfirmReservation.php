<?php

namespace App\Actions;

use App\Contracts\Execute;
use App\Enums\StatusEnum;
use App\Reservation;

class ConfirmReservation implements Execute
{
    /**
     * Create a new Reservation instance.
     */
    public function __construct(
        private Reservation $reservation,
    ) {}

    /**
     * Execute the action.
     */
    public function handle(): void
    {
        $this->reservation->setStatus(StatusEnum::CONFIRMED);

        $this->reservation->save();
    }
}
