from dataclasses import dataclass


@dataclass
class IGuardResult:
    succeeded: bool
    message: str


class Guard:
    @staticmethod
    def against_null_or_empty(argument: any) -> IGuardResult:
        """Verify null or empty data"""
        if argument == None and not argument:
            return IGuardResult(
                succeeded=False, message="{argument} is null or undefined"
            )

    @staticmethod
    def against_null_or_empty_bulk(**args) -> IGuardResult:
        """Verify multiple args if has a null or empty data"""

        for index in args:

            if not args[index]:
                return IGuardResult(
                    succeeded=False, message=f"{index} is null or undefined"
                )
