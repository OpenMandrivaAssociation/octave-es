%define	pkgname es
%define name	octave-%{pkgname}
%define version 0.0.4
%define release %mkrel 1

Summary:	Octave package for Spanish translations of functions
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{pkgname}-%{version}.tar.gz
Patch0:		es-compile-0.0.4.patch
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.net/es/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 2.9.9
BuildRequires:	octave-devel >= 2.9.9, MesaGL-devel, MesaGLU-devel

%description
This package provides support for the construction of Spanish language
translations of Octave functions.

%prep
%setup -q -c %{pkgname}-%{version}
tar zxf %SOURCE0 
%patch0 -p0
tar zcvf %{pkgname}-%{version}.tar.gz %{pkgname}

%install
rm -rf %{buildroot}
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
%__install -m 755 -d %{buildroot}%{_libdir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
export OCT_ARCH_PREFIX=%{buildroot}%{_libdir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX $OCT_ARCH_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

mv %{pkgname}/COPYING .
mv %{pkgname}/DESCRIPTION .

%clean
%__rm -rf %{buildroot}

%post
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%postun
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%files
%defattr(-,root,root)
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}
%{_libdir}/octave/packages/%{pkgname}-%{version}

