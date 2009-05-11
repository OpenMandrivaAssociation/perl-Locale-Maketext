
%define realname   Locale-Maketext
%define version    1.13
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Framework for software localization
Source:     http://www.cpan.org/modules/by-module/Locale/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(I18N::LangTags)
BuildRequires: perl(Test::More)

BuildArch: noarch

%description
It is a common feature of applications (whether run directly, or via the
Web) for them to be "localized" -- i.e., for them to a present an English
interface to an English-speaker, a German interface to a German-speaker,
and so on for all languages it's programmed with. Locale::Maketext is a
framework for software localization; it provides you with the tools for
organizing and accessing the bits of text and text-processing code that you
need for producing localized applications.

In order to make sense of Maketext and how all its components fit together,
you should probably go read Locale::Maketext::TPJ13, and _then_ read the
following documentation.

You may also want to read over the source for 'File::Findgrep' and its
constituent modules -- they are a complete (if small) example application
that uses Maketext.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_mandir}/man3/*
%perl_vendorlib/*


