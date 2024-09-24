# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2024 Valory AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This module contains the win_probability_threshold strategy."""

from typing import Dict, List, Union


def run(*_args, **kwargs) -> Dict[str, Union[int, List[str]]]:
    """Run the win probability threshold strategy."""
    bankroll = kwargs.get("bankroll", 0)
    win_probability = kwargs.get("win_probability", 0)
    threshold = kwargs.get("probability_threshold", 0.8)
    bet_percentage = kwargs.get("bet_percentage", 0.1)

    if win_probability > threshold:
        bet_amount = int(bankroll * bet_percentage)
        return {
            "bet_amount": bet_amount,
            "info": [
                f"Win probability {win_probability} above threshold {threshold}.",
                f"Betting {bet_percentage * 100}% of bankroll: {bet_amount / 10**18} xDAI.",
            ],
        }
    else:
        return {
            "bet_amount": 0,
            "info": [
                f"Win probability {win_probability} below threshold {threshold}. Not betting."
            ],
        }
