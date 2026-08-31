from dataclasses import dataclass, field


@dataclass
class Register:
    registrationId: int
    email: str
    phoneNumber: int
    userName: str
    password: str

    def create(self) -> str:
        return f"Registration created for {self.userName}"

    def authenticate(self, userName: str, password: str) -> bool:
        return self.userName == userName and self.password == password


@dataclass
class User:
    userId: int
    registrations: list[Register] = field(default_factory=list)

    def add(self, registration: Register) -> None:
        self.registrations.append(registration)

    def delete(self, registrationId: int) -> bool:
        for registration in self.registrations:
            if registration.registrationId == registrationId:
                self.registrations.remove(registration)
                return True
        return False


@dataclass
class Profile:
    profileId: int
    date: str
    activity: str
    description: str

    def show(self) -> str:
        return (
            f"Profile ID: {self.profileId}\n"
            f"Date: {self.date}\n"
            f"Activity: {self.activity}\n"
            f"Description: {self.description}"
        )


@dataclass
class LoginInformation:
    loginId: int
    userName: str
    password: str
    accountNumber: int
    profile: Profile | None = None

    def create(self) -> str:
        return f"Login information created for {self.userName}"

    def validate(self, userName: str, password: str) -> bool:
        return self.userName == userName and self.password == password

    def update(
        self,
        userName: str | None = None,
        password: str | None = None,
        accountNumber: int | None = None,
    ) -> None:
        if userName is not None:
            self.userName = userName

        if password is not None:
            self.password = password

        if accountNumber is not None:
            self.accountNumber = accountNumber

    def attach_profile(self, profile: Profile) -> None:
        self.profile = profile
