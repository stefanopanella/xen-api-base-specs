%global debug_package %{nil}

Name:           ocaml-ssl
Version:        0.5.2
Release:        2%{?dist}
Summary:        Use OpenSSL from OCaml
License:        LGPL
URL:            http://downloads.sourceforge.net/project/savonet/ocaml-ssl
Source0:        http://downloads.sourceforge.net/project/savonet/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  openssl-devel
BuildRequires:  autoconf
BuildRequires:  automake

%description
Use OpenSSL from OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       openssl-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
./bootstrap
./configure
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p $OCAMLFIND_DESTDIR/stublibs
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=%{buildroot}

%files
%doc CHANGES
%doc COPYING
%doc README.md
%{_libdir}/ocaml/ssl
%exclude %{_libdir}/ocaml/ssl/*.a
%exclude %{_libdir}/ocaml/ssl/*.cmxa
%exclude %{_libdir}/ocaml/ssl/*.cmx
%exclude %{_libdir}/ocaml/ssl/*.mli
%exclude %{_libdir}/ocaml/ssl/*.annot
%exclude %{_libdir}/ocaml/ssl/*.cmt
%exclude %{_libdir}/ocaml/ssl/*.cmti
%{_libdir}/ocaml/stublibs/dllssl_stubs.so
%{_libdir}/ocaml/stublibs/dllssl_stubs.so.owner
%{_libdir}/ocaml/stublibs/dllssl_threads_stubs.so
%{_libdir}/ocaml/stublibs/dllssl_threads_stubs.so.owner

%files devel
%{_libdir}/ocaml/ssl/*.a
%{_libdir}/ocaml/ssl/*.cmx
%{_libdir}/ocaml/ssl/*.cmxa
%{_libdir}/ocaml/ssl/*.mli

%changelog
* Wed Jul 27 2016 Euan Harris <euan.harris@citrix.com> - 0.5.2-2
- Remove *.cmt, *.cmti and *.annot

* Tue May 24 2016 Phus Lu <phus.lu@citrix.com> - 0.5.2-1
- Upgrade to ocaml-ssl-0.5.2 for TLSv1.2

* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 0.4.6-2
- Split files correctly between base and devel packages

* Sun Jun  2 2013 David Scott <dave.scott@eu.citrix.com> - 0.4.6-1
- Initial package

