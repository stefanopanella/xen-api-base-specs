%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:           ocaml-pa-ounit
Version:        112.35.00
Release:        2%{?dist}
Summary:        Syntax extension for in-line tests in code.

Group:          Development/Libraries
License:        Apache Software License 2.0
URL:            https://github.com/janestreet/pa_ounit
Source0:        https://ocaml.janestreet.com/ocaml-core/112.35/files/pa_ounit-%{version}.tar.gz
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 4.00.1
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-ounit-devel

%define _use_internal_dependency_generator 0
%define __find_requires /usr/lib/rpm/ocaml-find-requires.sh
%define __find_provides /usr/lib/rpm/ocaml-find-provides.sh


%description
Pa_ounit is a syntax extension that helps writing in-line tests in ocaml code.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n pa_ounit-%{version}

%build
ocaml setup.ml -configure --prefix %{_prefix} \
      --libdir %{_libdir} \
      --libexecdir %{_libexecdir} \
      --exec-prefix %{_exec_prefix} \
      --bindir %{_bindir} \
      --sbindir %{_sbindir} \
      --mandir %{_mandir} \
      --datadir %{_datadir} \
      --localstatedir %{_localstatedir} \
      --sharedstatedir %{_sharedstatedir}
ocaml setup.ml -build


%check
ocaml setup.ml -test


%install
rm -rf $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
ocaml setup.ml -install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE.txt  THIRD-PARTY.txt INRIA-DISCLAIMER.txt readme.md
%{_libdir}/ocaml/pa_ounit
%if %opt
%exclude %{_libdir}/ocaml/pa_ounit/*.a
%exclude %{_libdir}/ocaml/pa_ounit/*.cmxa
%endif
%exclude %{_libdir}/ocaml/pa_ounit/*.ml
%exclude %{_libdir}/ocaml/pa_ounit/*.mli
%exclude %{_libdir}/ocaml/pa_ounit/*.annot
%exclude %{_libdir}/ocaml/pa_ounit/*.cmt
%exclude %{_libdir}/ocaml/pa_ounit/*.cmti


%files devel
%defattr(-,root,root,-)
%doc LICENSE.txt  THIRD-PARTY.txt INRIA-DISCLAIMER.txt readme.md
%if %opt
%{_libdir}/ocaml/pa_ounit/*.a
%{_libdir}/ocaml/pa_ounit/*.cmxa
%endif
%{_libdir}/ocaml/pa_ounit/*.ml
%{_libdir}/ocaml/pa_ounit/*.mli


%changelog
* Wed Jul 27 2016 Euan Harris <euan.harris@citrix.com> - 112.35.00-2
- Remove *.cmt, *.cmti and *.annot

* Fri Jan 22 2016 Jon Ludlam <jonathan.ludlam@citrix.com> - 112.35.00-1
- Update to 112.35.00

* Tue Oct 14 2014 David Scott <dave.scott@citrix.com> - 111.28.00-1
- Update to 111.28.00

* Wed Jan 01 2014 Edvard Fagerholm <edvard.fagerholm@gmail.com> - 109.53.02-1
- Initial package for Fedora 20
