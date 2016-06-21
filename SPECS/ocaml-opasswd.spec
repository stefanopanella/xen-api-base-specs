Name:           ocaml-opasswd
Version:        1.0.1
Release:        1%{?dist}
Summary:        OCaml interface to the glibc passwd/shadow password functions
License:        ISC
URL:            https://github.com/xapi-project/ocaml-opasswd
Source0:        https://github.com/xapi-project/ocaml-opasswd/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  oasis
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ctypes-devel
BuildRequires:  libffi-devel

%description
This is an OCaml binding to the glibc passwd file and shadow password
file interface. It can be used to read, parse, manipulate and write
passwd and shadow files on Linux systems. It might also work on other
nixes, but it has not been tested.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-ctypes-devel%{?_isa}
Requires:       libffi%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
./configure --destdir %{buildroot}%{_libdir}/ocaml
make

%install
mkdir -p %{buildroot}%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
make install

%files
%doc README.md
%{_libdir}/ocaml/oPasswd
%exclude %{_libdir}/ocaml/oPasswd/*.a
%exclude %{_libdir}/ocaml/oPasswd/*.cmxa
%exclude %{_libdir}/ocaml/oPasswd/*.mli

%files devel
%{_libdir}/ocaml/oPasswd/*.a
%{_libdir}/ocaml/oPasswd/*.cmxa
%{_libdir}/ocaml/oPasswd/*.mli

%changelog
* Fri Jun 03 2016 Si Beaumont <simon.beaumont@citrix.com> - 1.0.1-1
- Update to 1.0.1
- New build dependency on OASIS

* Fri Apr 15 2016 Euan Harris <euan.harris@citrix.com> - 1.0.0-1
- Update to 1.0.0

* Thu May  1 2014 David Scott <dave.scott@citrix.com> - 0.9.3-1
- For -devel package add dependency on ocaml-ctypes-devel

* Thu Apr 24 2014 David Scott <dave.scott@citrix.com>
- Fix split between -devel and main package, hopefully

* Thu Oct 31 2013 Mike McClurg <mike.mcclurg@citrix.com>
- Initial package

